class Step2Form(AjaxForm):
    use_template = RadioSelectField(label=constant.LABEL_STEP2_FORM,
                                    choices=[("own", "Создать свою анкету"),
                                             ("template", "Использовать шаблон")],
                                    default="own")