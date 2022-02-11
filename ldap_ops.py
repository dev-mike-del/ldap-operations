#!/usr/bin/env python3
import ldap

LOGIN_DN = 'cn=read-only-admin,dc=example,dc=com'
LOGIN_PASSWORD = 'password'
SERVER_ADDRESS = 'ldap://ldap.forumsys.com'
get_user_example = """('uid=newton,dc=example,dc=com', {'sn': [b'Newton'], 'objectClass': [b'inetOrgPerson', b'organizationalPerson', b'person', b'top'], 'uid': [b'newton'], 'mail': [b'newton@ldap.forumsys.com'], 'cn': [b'Isaac Newton']})"""

class LdapOps(object):
    """
    The class "LdapOps" accepts three arguments (str). The class makes a 
    connection to an OpenLDAP source. The methods perform commonly needed
    tasks for maintaining and analyzing OpenLDAP data.
    """
    # Required: Login DN, Login Password and the OpenLDAP server address
    def __init__(self, LOGIN_DN:str, LOGIN_PASSWORD:str, SERVER_ADDRESS:str):
        """Set up an LdapOps object."""
        self.BIND_DN = LOGIN_DN
        self.BIND_PASSWORD = LOGIN_PASSWORD
        self.base_dn = 'dc=example, dc=com'
        self.ldap_connection = ldap.initialize(SERVER_ADDRESS)
        try:
            self.ldap_connection.simple_bind_s(self.BIND_DN,self.BIND_PASSWORD)
        except Exception as e:
            print("Try/Except >>> {}".format(e))
            raise e

    def get_user(self, username:str) -> tuple:
        """
        If user exists, returns a tuple. The tuple's first value is the
        user's dn. The second value is the user's attributes. If the user
        does not exist, return None.
        """
        user = self.ldap_connection.search_s(
                self.base_dn,
                ldap.SCOPE_SUBTREE,
                f'uid={username}',
                )
        try:
            return user[0]
        except IndexError:
            return None

    def user_exists(self, username:str) -> bool:
        """If user exists, return True. Else, return False"""
        try:
            user = self.get_user(username)
            if user[0]:
                return True
        except TypeError:
            return False

    def get_user_objectclass(self, username:str) -> list:
        """
        Call "self.get_user" method. If the user exists, return a list of
        the user's objectClasses. Example: ['inetOrgPerson',
        'organizationalPerson', 'person', 'top']
        """
        try:
            user = self.get_user(username)
            if user:
                return [x.decode() for x in user[1]['objectClass']]
            else:
                return f'{username} is not a valid uid in OpenLDAP'
        except Exception as e:
            print(e)

    def get_all_entries(self) -> list:
        """
        Return all entries from the base_dn using SCOPE_SUBTREE to include the
        objects and all its descendants.
        """
        results = self.ldap_connection.search_s(
                self.base_dn, 
                ldap.SCOPE_SUBTREE, 
                )
        return results

    def get_all_persons(self) -> list:
        """Return all entries with the objectClass of 'person'"""
        try:
            all_persons = self.ldap_connection.search_s(
                    self.base_dn,
                    ldap.SCOPE_SUBTREE,
                    ('objectClass=person'),
                    )
        except KeyError:
            pass
        return all_persons

    def get_all_emails(self) -> dict:
        """
        Return a dictionary of all email (mail) addresses from entries with
        the objectClass of 'person.' The dictionary contains two keys. The
        first key is "emails," and its value is a list of emails. The second key is
        "errors" and its value is a list of returned entries that did not
        include email addresses. 
        """
        try:
            all_emails = self.ldap_connection.search_s(
                    self.base_dn,
                    ldap.SCOPE_SUBTREE,
                    ('objectClass=person'),
                    ['mail'],
                    )
        except Exception:
            print(Exception)
        all_emails_clean = []
        errors = []
        for email in all_emails:
            try:
                all_emails_clean.append(email[1]['mail'][0].decode())
            except Exception as e:
                errors.append(email[0])
        return {'emails':all_emails_clean,'errors':errors}

