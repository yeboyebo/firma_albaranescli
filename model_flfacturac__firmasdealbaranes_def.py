# @class_declaration interna #
from YBLEGACY import qsatype


class interna(qsatype.objetoBase):

    ctx = qsatype.Object()

    def __init__(self, context=None):
        self.ctx = context


# @class_declaration firma_albaranescli #
from YBLEGACY.constantes import *


class firma_albaranescli(interna):

    def firma_albaranescli_getDesc(self):
        return None

    def firma_albaranescli_firmarAlbaran(self, oParam):
        print(oParam["base64Img"])
        usuario = qsatype.FLUtil.nameUser()
        params = self.dameAlbaranPorFirmar(usuario)
        if "firmado" in params and not params["firmado"]:
            curFirma = qsatype.FLSqlCursor(u"firmasdealbaranes")
            curFirma.select(u"id = {}".format(params["id"]))
            if curFirma.first():
                curFirma.setModeAccess(curFirma.Edit)
                curFirma.refreshBuffer()
                firma = oParam["base64Img"].split(",")
                imagen = firma[1]
                print("firmarAlbaran___imagen: ", imagen)
                curFirma.setValueBuffer("firma", imagen)
                curFirma.setValueBuffer("estado", "Aceptada")
            if not curFirma.commitBuffer():
                resul['status'] = -1
                resul['msg'] = "Error al firmar el albáran {}".format(params["codigo"])
                return resul
            if not qsatype.FLUtil.sqlUpdate(u"albaranescli", u"firmado", True, u"idalbaran = {}".format(params["idalbaran"])):
                return False
        return True

    def firma_albaranescli_drawif_labelPendiente(self, prefix):
        # Consultar si hay firmadealbaranes en estado X para el puesto del usuario logeado
        usuario = qsatype.FLUtil.nameUser()
        oParam = self.dameAlbaranPorFirmar(usuario)
        print("firmado__drawif_labelPendiente: ", oParam["firmado"])
        if "firmado" in oParam and not oParam["firmado"]:
            return "hidden"
        return ""

    def firma_albaranescli_drawif_firma(self, prefix):
        usuario = qsatype.FLUtil.nameUser()
        oParam = self.dameAlbaranPorFirmar(usuario)
        print("firmado__drawif_firma: ", oParam["firmado"])
        if "firmado" in oParam and oParam["firmado"]:
            return "hidden"

    def firma_albaranescli_dameAlbaranPorFirmar(self, usuario):
        params = {}
        print(usuario)
        params["firmado"] = True
        q = qsatype.FLSqlQuery()
        q.setTablesList(u"firmasdealbaranes")
        q.setSelect(u"id,idalbaran,codigo")
        q.setFrom(u"firmasdealbaranes")
        q.setWhere(u"estado = 'Pendiente' AND puesto = '{}'".format(usuario))

        if not q.exec_():
            print("Error inesperado")
            return params
        if q.first():
            params["firmado"] = False
            params["id"] = q.value("id")
            params["idalbaran"] = q.value("idalbaran")
            params["codigo"] = q.value("codigo")
            print("firmado: ", params["firmado"])
            print("id: ", params["id"])
            print("idalbaran: ", params["idalbaran"])
            print("codigo: ", params["codigo"])
        return params

    def __init__(self, context=None):
        super().__init__(context)

    def getDesc(self):
        return self.ctx.firma_albaranescli_getDesc()

    def firmarAlbaran(self, oParam):
        return self.ctx.firma_albaranescli_firmarAlbaran(oParam)

    def drawif_labelPendiente(self, prefix):
        return self.ctx.firma_albaranescli_drawif_labelPendiente(prefix)

    def drawif_firma(self, prefix):
        return self.ctx.firma_albaranescli_drawif_firma(prefix)

    def dameAlbaranPorFirmar(self, usuario):
        return self.ctx.firma_albaranescli_dameAlbaranPorFirmar(usuario)


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
