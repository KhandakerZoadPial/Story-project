from django.shortcuts import render
from .models import Stroy


# git commit -am "Backend accepting answers of questions & story is getting created" && git push

def home(request):
    if request.method=="POST":
        try:
            f = request
            date, birthplace, fullname, selected_by, why_named, nickname, nickname_why, mother_name, mother_birthdate, mother_birthplace, father_name, father_birthdate, father_birthplace, siblings_names, siblings_birth_places, number_of_sib, m_mother_name, m_mother_birthdate, m_father_name, m_father_birthdate, f_mother_name, f_mother_birthdate, f_father_name, f_father_birthdate  = story_helper(f)
            story = f"I was born on the {date} in {birthplace}, hospital"
            story = story + f"My full name is {fullname}."
            story = story + f"The people who decided on this name are {selected_by}."
            story = story + f"I was named this way because {why_named}."
            story = story + f"Sometimes, I go by the nickname {nickname} which I got from {nickname_why}"
            story = story + f"I have a beautiful mother named {mother_name}. She was born on {mother_birthdate} in {mother_birthplace}.The place she grew up in was lovely just like her."
            story = story + f"Meanwhile, my father, {father_name}, was born on the {father_birthdate}. He was raised in {father_birthplace}."
            story = story + f"Their names are {siblings_names}. They were born in {siblings_birth_places}."
            story = story + f"My mother was raised well by her parents. My grandmother was named {m_mother_name}. Her birthday was on {m_mother_birthdate}; whereas, my grandpa, {m_father_name}, was born on {m_father_birthdate}."
            story = story + f"On my father’s side, I was blessed with the lives of my grandma, {f_mother_name}, and my grandpa, {f_father_name}."
            obj = Stroy(owner=request.user, story_name='First Story', the_story=story)
            obj.save()
        except:
            pass
    
    return render(request, 'story/home.html')


def story_helper(req):
    date = req.POST.get('date')
    birthplace = req.POST.get('birthplace')
    fullname = req.POST.get('fullname')

    selected_by = req.POST.get('selected_by')
    why_named = req.POST.get('why_named')
    nickname = req.POST.get('nickname')
    nickname_why = req.POST.get('nickname_why')
    mother_name = req.POST.get('mother_name')
    mother_birthdate = req.POST.get('mother_birthdate')
    mother_birthplace = req.POST.get('mother_birthplace')
    father_name = req.POST.get('father_name')
    father_birthdate = req.POST.get('father_birthdate')
    father_birthplace = req.POST.get('father_birthplace')
    siblings_names = req.POST.get('siblings_names')
    siblings_birth_places = req.POST.get('siblings_birth_places')
    number_of_sib = req.POST.get('number_of_sib')
    m_mother_name = req.POST.get('m_mother_name')
    m_mother_birthdate = req.POST.get('m_mother_birthdate')

    m_father_name = req.POST.get('f_father_name')
    m_father_birthdate = req.POST.get('f_father_birthdate')

    f_mother_name = req.POST.get('f_mother_name')
    f_mother_birthdate = req.POST.get('f_mother_birthdate')

    f_father_name = req.POST.get('m_father_name')
    f_father_birthdate = req.POST.get('m_father_birthdate')
    
    return date, birthplace, fullname, selected_by, why_named, nickname, nickname_why, mother_name, mother_birthdate, mother_birthplace, father_name, father_birthdate, father_birthplace, siblings_names, siblings_birth_places, number_of_sib, m_mother_name, m_mother_birthdate, m_father_name, m_father_birthdate, f_mother_name, f_mother_birthdate, f_father_name, f_father_birthdate 
