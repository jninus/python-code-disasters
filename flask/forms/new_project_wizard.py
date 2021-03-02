from flask.forms.step_forms.step1_form import Step1Form
from flask.forms.step_forms.step2_form import Step2Form
from flask.utils import constant

"""
Weired implementation
"""
class NewProjectWizard(AjaxFormWizard):

    def context(self):
        return dict()

    step1_title = constant.STEP1_TITLE
    step2_title = constant.STEP2_TITLE

    def step1_context(self):
        can_create = True
        if current_user.demo and db.session.query(func.count(Project)).\
                                            filter(Project.user == current_user).\
                                            scalar() >= 1:
            can_create = False

        return dict(projects=db.session.query(Project).\
                                        filter_by(user=current_user).\
                                        all(),
                    actions_form=ProjectActionsForm(),
                    can_create=can_create)

    def step1_form(self):
        return Step1Form()

    def step2_form(self, data):
        return Step2Form()