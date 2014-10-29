import imaplib
import getpass
import email
def GetUnreadMail():

    conn_type = input("[1].IMAP4\n[2].IMAP4_SSL\n")
    if conn_type == 1:
    	conn = imaplib.IMAP4(raw_input("imapserver:\n"))#IMAP4 
    elif conn_type == 2:
    	conn = imaplib.IMAP4_SSL(raw_input("imapserver:\n"))#IMAP_SSL
    conn.login(raw_input("usrname:\n"),getpass.getpass("password:\n"))
    conn.list()
    conn.select('INBOX')
    fnvar = 0
    unreadflag,unreadlist = conn.search(None,'(UNSEEN)')
   	if unreadflag == 'OK':
      for message in unreadlist[0].split():
          stat,data = conn.fetch(message,'(RFC822)')
          msg = HeaderParser().parsestr(data[0][1])
          from_name = email.utils.parseaddr(msg['From'])[0]
          from_addr = email.utils.parseaddr(msg['From'])[1]
          Subject = msg['Subject']
          mail = email.message_from_string(data[0][1])
          payload=''
          for part in mail.walk():
            if part.get_content_subtype()=='plain':
                payload = part.get_payload()
          	if part.get('Content-Disposition') is None:
          		attachment = part.get_filename()
          		fp = open(from_addr+'_attach'+fnvar,'wb')
          		fp.write(part.get_payload(decode=True))
          		fp.close()
          		fnvar = fnvar+1
          		print ('attachment %sattach%s saved')%(from_addr,fnvar)
          body = payload.strip('\r\n')
    print ('from:%s\n email:%s\n content:%s\n') %(from_name,from_addr,body)

GetUnreadMail()