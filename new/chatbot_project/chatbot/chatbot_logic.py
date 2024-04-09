# user input
user_option=input("Enter you option:")
# user1="1"     #"How does solar work?"
# user2="2"   #"Will Solar save me money on my electric bill?"
# user3="3"        #"Is solar really free?"
# user4="4"          #"Other Question?"

options=["1","2","3","4"]
if user_option in options[:-1]:
    answer_index=options.index(user_option)
    answer=["""Solar works by taking the suns’ energy and converting it into usable power for your home. This is done
through the solar cells in the panels converting AC power into DC, usable power for your home, which is
converted through an inverter.
Most utility companies also offer something called Net Metering, which allows you to sell back the power to
the grid that you generate with solar, when your PV solar system generates more power than you need. Most
of the time, this will result in you getting a credit on your electric bill which can be used towards a future bill
in the less sunny months, when your system likely will not produce as much power. 

Would you like to find out your estimated savings with solar?""",

"""Saving money with solar depends on if your home is suitable for solar. The best way to know for sure is to
get it assessed. I can help with that as well! Homes that are suitable for solar will typically save thousands of
dollars over the lifespan of the panels (most new panels are warrantied for 25 years). Your home’s suitability
depends on its sun exposure, as well as roof type and angle. Also, your home will have to pass certain
structural and electrical code requirements.
I am happy to determine an estimated savings for your home with solar, and set you up with one of our
(R)VeraFied solar partners for a free home assessment. All of our partners are required to offer above
industry standard warranties, and meet Vera’s requirements for contractor conduct, support and ratings.

Would you like to set up an evaluation for your home?""",

"""When you hear “solar is free”, that is typically only referring to the installation of the panels, depending on
what program you go with (usually a lease or PPA program where you don’t purchase the panels.) A PPA is
also known as a power purchase agreement, where you agree to purchase power produced from the panels
at a steeply discounted rate from what your local utility company can provide. Typically most companies do
not charge installation fees for a PPA or leasing the system.
The alternative option is purchasing the panels through a loan or in cash. This option will typically yield you
the tax credits associated with solar, which are 30% of the purchase price through the year 2033. Most of the
time with a PPA and lease, the tax credits are already priced into the discount that the company gives you
on your monthly payment instead of you filing for the credit in your taxes. 

Would you like to find out your estimated savings with solar?"""
]
    response=answer[answer_index]
    print(response)

    user_option2=input("").casefold().strip()
    if user_option2=="yes":
        response2="""Sure, i am happy to help with that. First i will need a little bit of information about your
home. What is the address of your home?"""
        print(response2)
        user_address=input().casefold().strip()     #have to make this manage this address using ui 
        if user_address:
            response="OK great, and just to confirm, you are the homeowner correct?"
            print(response)

            user_owner_yes_no= input("").casefold().strip()
            if user_owner_yes_no=="yes":
                response="I will just need your first and last name to verify that. What is your name?"
                print(response)
                user_first_name=input("first name:")
                user_last_name=input("last name:")
                if user_first_name and user_last_name:
                    response=f"""Great {user_first_name}! What is the best email to send the proposal over to? I will have one of our VERAfied partners
reach out with the information.
I also need a good phone number. Is it okay for our partner to reach out via call or text with your
information?"""
                    print(response)
                    user_email=input("email address:")
                    user_mobil_number=input("user mobile number:")
                    user_communication_media=input("call or text:")
                    if user_email or user_mobil_number or user_communication_media:
                        response=f"{user_first_name} Thanks for information! May I know your average electricity bill?"
                        print(response)
                        user_electricity_info=eval(input())
                        if user_electricity_info:
                            #reducing 30% of average bill
                            reduced_bill=user_electricity_info*0.30
                            response=f"{user_first_name},\nyou can save upto ${reduced_bill} aproximate on your electricity bill. Shortly someone will reach you from Verafied Teams"
                            print(response)
                        else:
                            print("Not a valid bill detail.")
                        
            elif user_owner_yes_no=="no":
                response="""Are you the spouse or domestic partner of the home owner? We can only provide assessments on your
home in this case if you are a homeowner of the property. (say yes/no)"""
                user_homeowner_yes_no=input().casefold().strip()
                if user_homeowner_yes_no=="yes":
                    response="I will just need your first and last name to verify that. What is your name? "
                    print(response)
                    user_first_name=input("first name:")
                    user_last_name=input("last name:")
                    user_communication_media=input("call or text:")
                    if user_first_name and user_last_name:
                        response=f"""Great {user_first_name}! What is the best email to send the proposal over to? I will have one of our VERAfied partners
reach out with the information.
I also need a good phone number. Is it okay for our partner to reach out via call or text with your
information?""" 
                        user_email=input("email ID:")
                        user_mobil_number=input("user mobile number:")
                        user_communication_media=input("call or text:")
                    if user_email or user_mobil_number or user_communication_media:
                        response=f"{user_first_name} Thanks for information! May I know your average electricity bill?"
                        print(response)
                        user_electricity_info=eval(input())
                        #reducing 30% of average bill
                        reduced_bill=user_electricity_info*0.30
                        response=f"{user_first_name},\nyou can save upto ${reduced_bill} aproximate on your electricity bill. Shortly someone will reach you from Verafied Teams"
                        print(response)

                elif user_owner_yes_no=="no":
                    response="Thanks you for visit/interest.\n Have a wonderful day ahead"
                    print(response)
                else:
                    response="If you have something else in mind, please type it in the text box below."
                    print(response)
            else:
                response="Invalid option, If you have something else in mind, please type it in the text box below."

        else:
            response="This is not a valid location, If you have something else in mind, please type it in the text box below."      


            
    else:
        response2="If you have something else in mind, please type it in the text box below."

else:
    response="If you have something else in mind, please type it in the text box below."
    print(response)