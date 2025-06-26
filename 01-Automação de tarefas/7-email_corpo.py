from email.message import EmailMessage
import smtplib
import ssl

password = open('senha', 'r').read() #senha criada dentro do gmail para envio de email, precisa ser configurado antes.
from_email = 'martins.g3paulo@gmail.com' #email que esta enviando
to_email = 'martins.g3paulo@gmail.com,' #email que esta recebendo, pode ser para varios emails
subject = 'Proposta de parceria teste' #Assunto do email 
body = open('file/corpo.txt', 'r', encoding='utf-8').read()

#estruturando a mensagem via email
message = EmailMessage() # recebe uma instancia do EmailMessage
message['From'] = from_email 
message['To'] = to_email
message['Subject'] = subject

message.set_content(body) # conteudo do email
safe = ssl.create_default_context() #seguranca 

#envio do email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=safe) as smtp: 
    smtp.login(from_email, password) # faz o login via senha app criadao anteriormente, atraves do password
    smtp.sendmail(from_email, to_email, message.as_string()) #envia email
