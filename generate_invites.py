from jinja2 import Environment, FileSystemLoader
import os

guests = [
    # Друзья

    # 'Паравиз и Елена',
    # 'Эдуард и Анна',
    # 'Евгений и Ольга',
    # 'Артур и Ксения',
    # 'Альберт и Милена',

    # 'Михаил и Анастасия', #Мокины
    # 'Михаил и Елена', #Цаценко
    # 'Сергей и София' #Марчук
    # 'Диана'
    'Андрей',
    'Владислав',
    'Максим',
    'Сергей', 
    'Евгений',
    'Кирилл'



    # 'Ксюнечка',
    # Сеьмья

    # 'Комаровы',
    # 'Заварухины',
    # 'Киселёвы',
    # 'Захаровы',
    # 'Комаровы_Н'
    # 'Паньковы',
    # 'Соколовы',
    # 'бабушка и дедушка'
    # "Пятковы",
    # "мама и папа жениха",
    # "мама и папа невесты",
    # "Афанасьевы",
    # Добавьте остальных гостей
]

env = Environment(loader=FileSystemLoader('.'), autoescape=True)
template = env.get_template('template_single_m.html')

output_dir = 'invitations'
os.makedirs(output_dir, exist_ok=True)

for guest in guests:
    filename = f"{guest.replace(' ', '_').lower()}.html"
    context = {
        "guest_name": guest,
    }
    
    with open(os.path.join(output_dir, filename), 'w', encoding='utf-8') as f:
        f.write(template.render(context))

print(f"Сгенерировано {len(guests)} пригласительных страниц")