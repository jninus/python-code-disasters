__all__ = ["SOCIAL_QUESTIONS_IDS", "get_social_questions"]

# This one failed so badly:
SOCIAL_QUESTIONS_IDS = [1, 2, 15, 16, 17]



def get_social_questions():
 #   return [db.session.query(Question).get(q) for q in SOCIAL_QUESTIONS_IDS]

     # Presuming id is the primary key
     # Retrieving from an sql request is better than looping throw array
    return db.session.query(Question).filter(Question.id.in_(SOCIAL_QUESTIONS_IDS)).all()

