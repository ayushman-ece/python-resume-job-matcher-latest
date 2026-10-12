
from resume_matcher import match_resume


def main():
    print("=== Resume vs Job Description Matcher ===")

    resume = input("\nPaste a short resume summary: ").strip()
    job_description = input("\nPaste the job description: ").strip()

    if not resume or not job_description:
        print("Error: Both texts are required.")
        return

    result = match_resume(resume, job_description)

    print(f"\nText Similarity Score: {result['score']}%")

    print("\nShared Keywords:")
    if result["shared_keywords"]:
        print(", ".join(result["shared_keywords"]))
    else:
        print("No shared keywords found.")

    print("\nKeywords in job description not found in resume:")
    if result["missing_keywords"]:
        print(", ".join(result["missing_keywords"]))
    else:
        print("No missing keywords detected.")

    print("\nNote: Similarity is not a hiring probability or an ATS score.")


if __name__ == "__main__":
    main()
