import os
from django.core.management.base import BaseCommand
from apps.information.models import Biography

class Command(BaseCommand):
    help = 'Seeds the database with sample Biography data'

    def handle(self, *args, **kwargs):
        if Biography.objects.exists():
            self.stdout.write(self.style.WARNING('Biography already exists, skipped.'))
            return
        Biography.objects.create(
            description='{ "en": "<p>Feel free to reach out for <strong>job opportunities</strong>, <strong>collaborations</strong>, or any <strong>questions</strong>. I am always open to discussing <strong>new projects</strong>, <strong>ideas</strong>, or <strong>technologies</strong>.</p>", "es": "<p>No dudes en ponerte en contacto para <strong>oportunidades laborales</strong>, <strong>colaboraciones</strong> o cualquier <strong>pregunta</strong>. Siempre estoy abierto a discutir <strong>nuevos proyectos</strong>, <strong>ideas</strong> o <strong>tecnologías</strong>.</p>"}',
            stacks_description='{ "en": "<p>Skilled in <strong>JavaScript</strong>, <strong>TypeScript</strong>, <strong>ReactJS</strong>, <strong>Laravel</strong>, and <strong>NodeJS</strong>. Experienced with <strong>PostgreSQL</strong>, <strong>MongoDB</strong>, and <strong>MySQL</strong>. Proficient in <strong>Git</strong>, <strong>Jira</strong>, <strong>Docker</strong>, and <strong>AWS</strong>. Familiar with <strong>Agile (Scrum)</strong> workflows.</p>", "es": "<p>Hábil en <strong>JavaScript</strong>, <strong>TypeScript</strong>, <strong>ReactJS</strong>, <strong>Laravel</strong> y <strong>NodeJS</strong>. Experiencia con <strong>PostgreSQL</strong>, <strong>MongoDB</strong> y <strong>MySQL</strong>. Proficiente en <strong>Git</strong>, <strong>Jira</strong>, <strong>Docker</strong> y <strong>AWS</strong>. Familiarizado con flujos de trabajo <strong>ágiles (Scrum)</strong>.</p>" }',
            about_me='{ "en": "<p>I am a <strong>full stack software developer</strong> with over <strong>3 years</strong> of professional experience specializing in <strong>React.js</strong>, <strong>Node.js</strong>, <strong>PHP</strong>, <strong>Laravel</strong>, and <strong>Angular</strong>. I am currently focused on developing <strong>web applications</strong> for <strong>financial</strong> and <strong>business processes</strong> and continuously seek new knowledge and <strong>technological projects</strong>. I am looking for a position as a <strong>backend</strong> or <strong>frontend developer</strong> to grow in a professional environment.</p>", "es": "<p>Soy un <strong>desarrollador de software full stack</strong> con más de <strong>3 años</strong> de experiencia profesional, especializado en <strong>React.js</strong>, <strong>Node.js</strong>, <strong>PHP</strong>, <strong>Laravel</strong> y <strong>Angular</strong>. Actualmente, me concentro en desarrollar <strong>aplicaciones web</strong> orientadas a <strong>procesos financieros</strong> y <strong>empresariales</strong>, y estoy en constante búsqueda de <strong>nuevos conocimientos</strong> y <strong>proyectos tecnológicos</strong>. Estoy buscando un cargo como <strong>desarrollador backend</strong> o <strong>frontend</strong> que me permita crecer en un entorno profesional.</p>" }',
            phone_1=os.getenv('PHONE_NUMBER', 'default_phone_1'),
            phone_2=os.getenv('PHONE_NUMBER', 'default_phone_2'),
            email_1=os.getenv('CONTACT_EMAIL', 'default_email_1@example.com'),
            email_2=os.getenv('CONTACT_EMAIL_ALTERNATIVE', 'default_email_2@example.com')
        )
        self.stdout.write(self.style.SUCCESS('Successfully seeded the database with Biography data'))
