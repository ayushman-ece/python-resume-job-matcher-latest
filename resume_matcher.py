
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def match_resume(resume, job_description):
    vectorizer = TfidfVectorizer(stop_words="english")

    vectors = vectorizer.fit_transform(
        [resume, job_description]
    )

    score = round(
        cosine_similarity(vectors[0], vectors[1])[0][0] * 100,
        2
    )

    words = vectorizer.get_feature_names_out()
    resume_vector = vectors[0].toarray()[0]
    job_vector = vectors[1].toarray()[0]

    resume_keywords = {
        words[i] for i, value in enumerate(resume_vector) if value > 0
    }
    job_keywords = {
        words[i] for i, value in enumerate(job_vector) if value > 0
    }

    shared_keywords = sorted(resume_keywords & job_keywords)
    missing_keywords = sorted(job_keywords - resume_keywords)

    return {
        "score": score,
        "shared_keywords": shared_keywords,
        "missing_keywords": missing_keywords,
    }
