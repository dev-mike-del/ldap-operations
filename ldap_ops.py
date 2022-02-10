from collections import OrderedDict
import ldap

LOGIN_DN = 'cn=read-only-admin,dc=example,dc=com'
LOGIN_PASSWORD = 'password'
SERVER_ADDRESS = 'ldap://ldap.forumsys.com'

class LDAPOps(object):
    """Makes a connection to OpenLDAP and offers useful function."""
    def __init__(self, LOGIN_DN=LOGIN_DN, LOGIN_PASSWORD=LOGIN_PASSWORD, SERVER_ADDRESS=SERVER_ADDRESS):
        """Set up an LDAPOps object."""
        self.BIND_DN = LOGIN_DN
        self.BIND_PASSWORD = LOGIN_PASSWORD
        self.base_dn = 'dc=example, dc=com'
        self.ldap_connection = ldap.initialize(SERVER_ADDRESS)
        try:
            self.ldap_connection.simple_bind_s(self.BIND_DN, self.BIND_PASSWORD)
        except Exception as e:
            print("Try/Except >>> {}".format(e))
            raise e

    def get_user(self, username):
        user = self.ldap_connection.search_s(
                self.base_dn,
                ldap.SCOPE_SUBTREE,
                f'uid={username}',
                )
        try:
            return user[0]
        except IndexError:
            return None

    def user_exists(self, username):
        try:
            user = self.get_user(username)
            if user[0]:
                return True
        except TypeError:
            return False

    def get_user_objectclass(self, username):
        try:
            user = self.get_user(username)
            if user:
                return [x.decode() for x in user[1]['objectClass']]
            else:
                return f'{username} is not a valid uid in OpenLDAP'
        except Exception as e:
            print(e)

    def get_all_entries(self):
        results = self.ldap_connection.search_s(
                self.base_dn, 
                ldap.SCOPE_SUBTREE, 
                )
        return [x for x in results]

    def get_all_persons(self):
        try:
            all_persons = self.ldap_connection.search_s(
                    self.base_dn,
                    ldap.SCOPE_SUBTREE,
                    ('objectClass=person'),
                    )
        except KeyError:
            pass
        return all_persons

    def get_all_emails(self):
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
