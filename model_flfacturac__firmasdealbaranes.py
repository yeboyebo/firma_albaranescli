# @class_declaration interna_firmasdealbaranes #
import importlib
from YBLEGACY import qsatype

from YBUTILS.viewREST import helpers

from models.flfacturac import models as modelos


class interna_firmasdealbaranes(modelos.mtd_firmasdealbaranes, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration firma_albaranescli_firmasdealbaranes #
class firma_albaranescli_firmasdealbaranes(interna_firmasdealbaranes, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration firmasdealbaranes #
class firmasdealbaranes(firma_albaranescli_firmasdealbaranes, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface

    @helpers.decoradores.accion(aqparam=["oParam"])
    def firmarAlbaran(self, oParam):
        return form.iface.firmarAlbaran(oParam)

    def drawif_labelPendiente(prefix):
        print("??????")
        return form.iface.drawif_labelPendiente(prefix)

    def drawif_firma(prefix):
        return form.iface.drawif_firma(prefix)


definitions = importlib.import_module("models.flfacturac.firmasdealbaranes_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
