class User:
    def __init__(self, user_email, user_name, passwrod, current_job_title):
        self.email = user_email
        self.name = user_name
        self.password = passwrod
        self.current_job_title = current_job_title

    def change_user_current_job(self, new_job_title):
        self.current_job_title = new_job_title
    def change_password(self, new_password):
        self.password = new_password

    def get_user_info(self):
        print(f"User {self.name} currently works as a {self.current_job_title}. "
              f"You contact them at {self.email}")

