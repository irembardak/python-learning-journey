# --- Quick bio script to track my CS journey ---

def get_profile():
    profile_data = {
        "candidate": "Irem Bardak",
        "focus_area": "Computer Engineering & AI",
        "current_status": "Active Learning & Building",
        "stack": ["Python", "Logic Design", "Algorithms"]
    }
    
    print(f"--- {profile_data['candidate']} | Engineering Profile ---")
    print(f"Specialization: {profile_data['focus_area']}")
    print(f"Status: {profile_data['current_status']}")
    print(f"Initial Stack: {', '.join(profile_data['stack'])}")

if __name__ == "__main__":
    get_profile()
    print("\n[System] Profile rendered successfully.")
