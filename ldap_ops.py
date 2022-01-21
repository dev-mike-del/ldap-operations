import ldap, os, smbpasswd, base64, hashlib
import ldap.modlist as modlist


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
        self.ldap_connection = ldap.initialize(server_address)
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
