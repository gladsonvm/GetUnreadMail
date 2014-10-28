GetUnreadMail
=============

Python script to Fetch unread emails

This is a simple python script to check and fetch unread email over an unencrypted connection. 
To use it over an encrypted connection change IMAP4 to IMAP4_SSL.
Currently search for INBOX folder and check for unread messages using the 'UNSEEN' flag.
Libraries used: imaplib,email
