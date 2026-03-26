import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('stopwords', quiet=True)

CAREER_MAP = {
    "data scientist": ["python", "machine learning", "data analysis", "statistics", "pandas", "numpy", "visualization"],
    "web developer": ["html", "css", "javascript", "react", "backend", "database", "api"],
    "software engineer": ["java", "python", "c++", "algorithms", "data structures", "debugging", "oop"]
}

def clean_text(text):
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text.lower())

    return {word for word in tokens if word.isalnum() and word not in stop_words}

def analyze_profile(resume_text, target_role):
    resume_keywords = clean_text(resume_text)
    required_skills = CAREER_MAP.get(target_role, [])
    
    if not required_skills:
        return None

    found = [skill for skill in required_skills if skill in resume_keywords]
    missing = [skill for skill in required_skills if skill not in resume_keywords]
    
    match_percentage = (len(found) / len(required_skills)) * 100
    return found, missing, match_percentage

def main():
    print("Career Match Scouter")
    available_roles = ", ".join(CAREER_MAP.keys())
    print(f"Available Roles: {available_roles}")

    role = input("\nWhat role are you aiming for? ").strip().lower()

    if role not in CAREER_MAP:
        print(f"Sorry, I don't have data for '{role}' yet. Try: {available_roles}")
        return

    print(f"\nPaste your resume content (Press Enter when done):")
    user_resume = input("> ")

    result = analyze_profile(user_resume, role)
    
    if result:
        found, missing, score = result
        
        print(f"\n{'='*30}")
        print(f"Analysis for: {role.title()}")
        print(f"Match Score: {score:.1f}%")
        print(f"{'='*30}")

        if found:
            print(f"Skills detected: {', '.join(found)}")
        
        if missing:
            print(f"\nAreas to improve:")
            for skill in missing:
                print(f" • Consider adding/learning: {skill.title()}")
        else:
            print("\nPerfect match! Your resume covers all the key bases.")

if __name__ == "__main__":
    main()