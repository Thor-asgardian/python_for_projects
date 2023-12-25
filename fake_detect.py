def is_fake_account(username, followers, following, bio):
def any(not c.isalnum() for c in username):
    return True


    if "user" in username or "fake" in username:
        return True

    # You can adjust these thresholds based on typical ratios for legitimate accounts
    followers_to_following_ratio = followers / following
    if followers_to_following_ratio < 0.1:
        return True  # Suspiciously low followers-to-following ratio

    # You can add more sophisticated checks based on the content of the bio
    if "spam" in bio or "fake" in bio:
        return True

    return False

def main():
    username = input("Enter the social media account username: ")

    # For simplicity, let's assume the number of followers and following and the bio are known
    followers = int(input("Enter the number of followers: "))
    following = int(input("Enter the number of following: "))
    bio = input("Enter the bio: ")

    if is_fake_account(username, followers, following, bio):
        print("This social media account may be fake.")
    else:
        print("This social media account seems legitimate.")

if __name__ == "__main__":
    main()
