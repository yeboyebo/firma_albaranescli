# @class_declaration interna_puestosdefirma #
import importlib

from YBUTILS.viewREST import helpers

from models.flfacturac import models as modelos


class interna_puestosdefirma(modelos.mtd_puestosdefirma, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration firma_albaranescli_puestosdefirma #
class firma_albaranescli_puestosdefirma(interna_puestosdefirma, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    @helpers.decoradores.accion(aqparam=["oParam"])
    def establecerPuesto(self, oParam):
        return form.iface.establecerPuesto(self, oParam)

    def comprobarPuesto(cursor):
        return form.iface.comprobarPuesto(cursor)


# @class_declaration puestosdefirma #
class puestosdefirma(firma_albaranescli_puestosdefirma, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfacturac.puestosdefirma_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
