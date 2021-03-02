class Step1Form(AjaxForm):
    title = fields.TextField(label=constant.LABEL_STEP1_FORM, validators=[validators.Required()])