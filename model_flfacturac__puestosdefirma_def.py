# @class_declaration interna #
from YBLEGACY import qsatype


class interna(qsatype.objetoBase):

    ctx = qsatype.Object()

    def __init__(self, context=None):
        self.ctx = context


# @class_declaration firma_albaranescli #
from YBLEGACY.constantes import *
from YBUTILS.viewREST import cacheController


class firma_albaranescli(interna):

    def firma_albaranescli_getDesc(self):
        return None

    def firma_albaranescli_establecerPuesto(self, model, oParam):
        aChecked = oParam['selecteds'].split(u",")
        response = {}
        response['status'] = 1
        if len(aChecked) > 1:
            response['msg'] = "Error: Selecciona solo un elemento"
            return response
        if not aChecked[0]:
            response['msg'] = "Error: Selecciona un elemento"
            return response

        print("Puesto: ", aChecked[0])
        cacheController.setSessionVariable(ustr(u"puestodefirma_", qsatype.FLUtil.nameUser()), aChecked[0])
        return True

    def firma_albaranescli_comprobarPuesto(self, cursor):
        puesto = cacheController.getSessionVariable(ustr(u"puestodefirma_", qsatype.FLUtil.nameUser()))
        print("firma_albaranescli_comprobarPuesto: ", puesto)
        if puesto:
            return False
        return True

    def __init__(self, context=None):
        super().__init__(context)

    def getDesc(self):
        return self.ctx.firma_albaranescli_getDesc()

    def establecerPuesto(self, model, oParam):
        return self.ctx.firma_albaranescli_establecerPuesto(model, oParam)

    def comprobarPuesto(self, cursor):
        return self.ctx.firma_albaranescli_comprobarPuesto(cursor)


# @class_declaration head #
class head(firma_albaranescli):

    def __init__(self, context=None):
        super().__init__(context)


# @class_declaration ifaceCtx #
class ifaceCtx(head):

    def __init__(self, context=None):
        super().__init__(context)


# @class_declaration FormInternalObj #
class FormInternalObj(qsatype.FormDBWidget):
    def _class_init(self):
        self.iface = ifaceCtx(self)
