import os, sys, json, requests, time

def main():
    def banner():
        BANNER = f"""
        ███████ ██ ███████ ██   ██ ████████  ██████   ██████  ██      
        ██      ██ ██      ██   ██    ██    ██    ██ ██    ██ ██      
        █████   ██ ███████ ███████    ██    ██    ██ ██    ██ ██      
        ██      ██      ██ ██   ██    ██    ██    ██ ██    ██ ██      
        ██      ██ ███████ ██   ██    ██     ██████   ██████  ███████ 
                                                            @bootlegfish
                                                  github.com/thebtlgfish
                                                   thebtlgfish.github.io
        """
        print(BANNER)

    def again():
        time.sleep(2)
        print("\nWould You Like To Chose Another Program Again? (y/n): ")
        user_choice = input()
        if os.name == 'posix':
            os.system("clear")
        elif os.name == 'nt':
            os.system("cls")
        if user_choice == 'y':
              if os.name == 'posix':
                os.system("clear")
                main()
              elif os.name == 'nt':
                os.system("cls")
                main()
        elif user_choice == 'n':
              if os.name == 'posix':
                os.system("clear")
              elif os.name == 'nt':
                os.system("cls")
                
                sys.exit(0)
        elif user_choice != 'n' or 'y':
              print("Invalid Answer Chose Again")
              again_else()
              


    def again_else():
         time.sleep(2)
         print("\nWould You Like To Chose Another Program Again? (y/n): ")
         user_choice = input()
         if user_choice == 'y':
            if os.name == 'posix':
                os.system("clear")
                main()
            elif os.name == 'nt':
                os.system("cls")
                main()
            elif user_choice == 'n':
              if os.name == 'posix':
                os.system("clear")
              elif os.name == 'nt':
                os.system("cls")
                sys.exit(0)


    
    def user_help():
        print("Welcome To The Fish Multitool, A Simple And Easy Way To Get Tasks Done More Effectively! Made By BootlegFish, This Is A Pretty Basic But Useful Program")
        again()

    
    def send_webhook():

        print("Enter The Webhook Url: ")
        WEBHOOK_URL = input()
        print("Enter The Message Content: ")
        message = input()
        print("Enter Webhook Bot Username: ")
        username = input()
        print("Enter Webhook Avatar Url (Optional): ")
        avatar_url = input()

        data = {
            "content": message,
            "username": username,
            "avatar_url": avatar_url,
        }

        response = requests.post(WEBHOOK_URL, json=data)

        if response.status_code == 204:
                print("Message sent successfully!")
        else:
                print(f"Failed to send message: {response.status_code}")

        time.sleep(2)
        again()


        
    def spam_webhook():
        print("Enter The Webhook Url: ")
        WEBHOOK_URL = input()
        print("Enter The Message Content: ")
        message = input()
        print("Enter Webhook Bot Username: ")
        username = input()
        print("Enter Webhook Avatar Url (Optional): ")
        avatar_url = input()

        data = {
            "content": message,
            "username": username,
            "avatar_url": avatar_url,
            }

        response = requests.post(WEBHOOK_URL, json=data)

        while True:
            if response.status_code == 204:
                    print("Message sent successfully!")
            else:
                    print(f"Failed to send message: {response.status_code}")
        
        
        again()
    

    def webhook_info():
         print("\n Enter Webhook Url: ")
         WEBHOOK_URL = input()
         webhook_info_command = f"curl --max-time 10 {WEBHOOK_URL}"
         os.system(webhook_info_command)

         again()

         

    

    def userinput():
        print("Options: \n 0. Exit \n 1. Info \n 2. Send A Discord Webhook \n 3. Spam A Discord Webhook \n 4. Find Webhook Information")
        choice = input()
        if choice == '0':
            sys.exit(0)
        elif choice == '1':
            user_help()
        elif choice == '2':    
            send_webhook()
        elif choice == '3':
            spam_webhook()
        elif choice == '4':
            webhook_info()



    
    banner()
    userinput()




main()

            
