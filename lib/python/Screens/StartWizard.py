from Wizard import wizardManager
from Screens.WizardLanguage import WizardLanguage
from Screens.VideoWizard import VideoWizard
from Screens.Rc import Rc
from Screens.Screen import Screen
from boxbranding import getBoxType
from Components.Pixmap import Pixmap
from Components.config import config, ConfigBoolean, configfile
from LanguageSelection import LanguageWizard
config.misc.firstrun = ConfigBoolean(default=True)
config.misc.languageselected = ConfigBoolean(default=True)
config.misc.videowizardenabled = ConfigBoolean(default=True)

class StartWizard(WizardLanguage, Rc):

    def __init__(self, session, silent = True, showSteps = False, neededTag = None):
        self.xmlfile = ['startwizard.xml']
        WizardLanguage.__init__(self, session, showSteps=False)
        Rc.__init__(self)
        self['wizard'] = Pixmap()
        self['HelpWindow'] = Pixmap()
        self['HelpWindow'].hide()
        Screen.setTitle(self, _('StartWizard'))

    def markDone(self):
        if getBoxType() == 'dm8000':
            config.misc.rcused.value = 0
        else:
            config.misc.rcused.value = 1
        config.misc.rcused.save()
        config.misc.firstrun.value = 0
        config.misc.firstrun.save()
        configfile.save()


wizardManager.registerWizard(LanguageWizard, config.misc.languageselected.getValue(), priority=0)
wizardManager.registerWizard(VideoWizard, config.misc.videowizardenabled.getValue(), priority=2)
wizardManager.registerWizard(StartWizard, config.misc.firstrun.getValue(), priority=20)
