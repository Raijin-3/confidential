from django.http import JsonResponse
from django.shortcuts import render

def chat_question(request):
    return render(request, "chat.html")

def chat(request, button_id):
    # Define responses for each button ID
    if button_id == 'how-solar-works':
        response_text = """Vera: Solar works by taking the sun's energy and converting it into usable power for your home. 
        This is done through the solar cells in the panels converting AC power into DC, usable power for your home, which is converted
        through an inverter. Most utility companies also offer something called Net Metering, which allows you to sell back the power to 
        the grid that you generate with solar, when your PV solar system generates more power than you need. Most of the time, this will 
        result in you getting a credit on your electric bill which can be used towards a future bill in the less sunny months, when your 
        system likely will not produce as much power.\n 
        Would you like to find out your estimated savings with solar?(yes/no)"""

        # Check if the user responded with "yes"

        user_response = request.GET.get('message','').casefold().strip()   #this should execute first then after checking the condition second if should excute 
        if button_id == 'how-solar-works' and user_response=="yes":
            response_text = "Sure, I am happy to help with that. First, I will need a little bit of information about your home. What is the address of your home?"
            
            user_address2=request.GET.get('message','').casefold().strip()     #have to make this manage this address using ui 
            if button_id == 'how-solar-works' and user_response=="yes" and user_address2 not in ["yes","no","Yes","No"]:
                print(user_address2.isalpha(),user_address2)
                response_text="OK great, and just to confirm, you are the homeowner correct?"
                
                user_owner_yes_no= request.GET.get('message','').casefold().strip()
                if user_owner_yes_no=="yes":
                    response_text="I will just need your first and last name to verify that. What is your full name?"
                    # db_store=split the name into two part and first_name last_name 
                    user_full_name=request.GET.get('message','').casefold().strip()
                    
                    if user_full_name:
                        response_text=f"""Great {user_full_name.split()[0]}! What is the best email to send the proposal over to? I will have one of our VERAfied partners
                                          reach out with the information.
                                          I also need a good phone number. Is it okay for our partner to reach out via call or text with your
                                          information?"""
                        
                        user_email=request.GET.get('message','').casefold().strip()
                        user_mobil_number=request.GET.get('message','').casefold().strip()
                        user_communication_media=request.GET.get('message','').casefold().strip()
                        if user_email or user_mobil_number or user_communication_media:
                            response_text=f"{user_full_name.split()[0]} Thanks for information! May I know your average electricity bill?"
                            
                            user_electricity_info=request.GET.get('message','').casefold().strip()
                            if user_electricity_info:
                                #reducing 30% of average bill
                                reduced_bill=user_electricity_info*0.30
                                response_text=f"{user_full_name.split()[0]},\nyou can save upto ${reduced_bill} aproximate on your electricity bill. Shortly someone will reach you from Verafied Teams"
                            else:
                                response_text="Not a valid bill details.Thanks have a nice day"   # have to modify the context once the bot will ready

                elif user_owner_yes_no=="no":
                    response_text="""Are you the spouse or domestic partner of the home owner? We can only provide assessments on your
                                home in this case if you are a homeowner of the property. (say yes/no)"""
                    user_homeowner_yes_no=request.GET.get('message','').casefold().strip()
                    if user_homeowner_yes_no=="yes":
                        response_text="I will just need your first and last name to verify that. What is your name? "
                   

    elif button_id == 'save-money':
        response_text = """Vera: Saving money with solar depends on if your home is suitable for solar. The best way to know for sure is to get it assessed. 
        I can help with that as well! Homes that are suitable for solar will typically save thousands of dollars over the lifespan of the panels 
        (most new panels are warrantied for 25 years). Your home’s suitability depends on its sun exposure, as well as roof type and angle. Also, your 
        home will have to pass certain structural and electrical code requirements. I am happy to determine an estimated savings for your home with solar, 
        and set you up with one of our VERAfied solar partners for a free home assessment. All of our partners are required to offer above industry standard 
        warranties, and meet Vera’s requirements for contractor conduct, support and ratings. Would you like to set up an evaluation for your home?"""
    elif button_id == 'solar-is-free':
        response_text = """Vera: When you hear “solar is free”, that is typically only referring to the installation of the panels, depending on
        what program you go with (usually a lease or PPA program where you don’t purchase the panels.) A PPA is
        also known as a power purchase agreement, where you agree to purchase power produced from the panels
        at a steeply discounted rate from what your local utility company can provide. Typically most companies do
        not charge installation fees for a PPA or leasing the system.
        The alternative option is purchasing the panels through a loan or in cash. This option will typically yield you
        the tax credits associated with solar, which are 30% of the purchase price through the year 2033. Most of the
        time with a PPA and lease, the tax credits are already priced into the discount that the company gives you
        on your monthly payment instead of you filing for the credit in your taxes. 

        Would you like to find out your estimated savings with solar?"""
    else:
        response_text = "No specific response for this button yet."

    # Return response as JSON
    return JsonResponse({'response': response_text})
