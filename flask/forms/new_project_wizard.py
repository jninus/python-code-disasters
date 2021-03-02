from flask.utils import constant


class NewProjectWizard(AjaxFormWizard):
    def __init__(self):  # nice one.
        pass

    def context(self):
        return dict()

    step1_title = constant.STEP1_TITLE

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
        class Step1Form(AjaxForm):
            title       = fields.TextField(label=constant.LABEL_STEP1_FORM, validators=[validators.Required()])

        return Step1Form()

    step2_title = constant.STEP2_TITLE

    def step2_form(self, data):  # class is defined inside method (?!):
        class Step2Form(AjaxForm):
            #parameters      = create_parameter_groups_select_field(db.session.query(Industry).get(data["1"]["industry"]))
            use_template    = RadioSelectField(label=constant.LABEL_STEP2_FORM,
                                               choices=[("own", "Создать свою анкету"),
                                                        ("template", "Использовать шаблон")],
                                               default="own")

        return Step2Form()