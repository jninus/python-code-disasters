"""
Original commit message was: 'fuck fuck fuck'.
"""
from flask.utils import constant


"""
    This code does absolutely nothing, 
    No return or modification is done !!!!!!!!!!!!!!!!!!!!!!
"""
@app.route("/url/<int:id>/type/<any(html, xlsx):format>")
@role_required("specialist")
def project_results(id, format):
    project = get_my_project(id)

    report_builder = get_report_builder(project, format)

    if project.id == constant.CUSTOM_PROJECT_ID:  # thx the universe, we have only one custom project.
        colors_iterator = itertools.cycle((color for color in bg_colors if color != "ffffff"))
        questionnaire_colors = {}
        questions_answers = defaultdict(lambda: [])
        questions_answers_colors = defaultdict(lambda: [])
        for questionnaire in db.session.query(Questionnaire).filter_by(project=project):
            answers = db.session.query(QuestionnaireAnswer).filter_by(questionnaire=questionnaire)

            for answer in answers:
                if answer.question.id == constant.ANSWER_CUSTOM_ID:  # and one custom question.
                    if answer.answer not in questionnaire_colors:
                        questionnaire_colors[answer.answer] = "#%s" % colors_iterator.next()
                    questionnaire_color = questionnaire_colors[answer.answer]
                    break
            else:
                questionnaire_color = constant.BLACK_COLOR

            for answer in answers:
                if answer.answer is not None:
                    questions_answers[answer.question].append(answer.answer)
                    questions_answers_colors[answer.question].append(questionnaire_color)
    else:
        handle_normal()