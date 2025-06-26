from email.message import EmailMessage
import smtplib
import ssl
import mimetypes

password = open('senha', 'r').read() #senha criada dentro do gmail para envio de email, precisa ser configurado antes.
from_email = 'martins.g3paulo@gmail.com' #email que esta enviando
to_email = 'martins.g3paulo@gmail.com,' #email que esta recebendo, pode ser para varios emails
subject = 'Proposta de parceria teste' #Assunto do email 
body = open('file/index.html.txt', 'r', encoding='utf-8').read()

#estruturando a mensagem via email
message = EmailMessage() # recebe uma instancia do EmailMessage
message['From'] = from_email 
message['To'] = to_email
message['Subject'] = subject

message.set_content(body, subtype='html') # conteudo do email
safe = ssl.create_default_context() #seguranca 

#Adicionando anexo
anexo = 'file/test.pdf' #diretorio do arquivo
print(mimetypes.guess_type(anexo)[0])
mime_type, mime_subtype = mimetypes.guess_type(anexo)[0].split('/')
with open(anexo, 'rb') as a:
    message.add_attachment(
        a.read(),
        maintype=mime_type,
        subtype=mime_subtype,
        filename=anexo
    )

#envio do email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=safe) as smtp:
    smtp.login(from_email, password)
    smtp.sendmail(from_email, to_email, message.as_string())