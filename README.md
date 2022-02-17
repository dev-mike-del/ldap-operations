<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
<!--   <a href="https://github.com/github_username/repo_name">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a> -->

<h1 align="center">LDAP Operations</h1>

  <p align="center">
    Python script that performs basic LDAP searches.
<!--     <br />
    <a href="https://github.com/github_username/repo_name"><strong>Explore the docs »</strong></a>
    <br /> -->
    <br />
<!--     <a href="https://github.com/github_username/repo_name">View Demo</a> -->
    ·
    <a href="https://github.com/dev-mike-del/ldap_operations/issues">Report Bug</a>
    ·
    <a href="https://github.com/dev-mike-del/ldap_operations/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Python Interpreter Example Screen Shot][python_interpreter_example-screenshot]](https://docs.python.org/3/tutorial/interpreter.html)

This project offers the script ldap_ops.py as a developer tool for easy to use and straight foward LDAP queries. The script contains the class LDAPOps. That class creates a connection to an OpenLDAP server and maintains that connection for use through out the Class methods. The class methods use the LDAP connection to perform searches/queries using the search/queries provide by the Python library python-ldap.

The repo uses Forum Systems' LDAP Test Server to demonstrate how the search functions work on a live OpenLDAP server.

Methods:
* get_user(self, username:str) -> tuple:
    * If user exists, returns a tuple. The tuple's first value is the
        user's dn. The second value is the user's attributes. If the user
        does not exist, return None.

* user_exists(self, username:str) -> bool:
    * If user exists, return True. Else, return False

* get_all_user_objectclass(self, username:str) -> list
    * Call "self.get_user" method. If the user exists, return a list of
        the user's objectClasses. 
    * Return Example: ['inetOrgPerson','organizationalPerson', 'person', 'top']

* get_all_entries(self) -> list:
    * Return all entries from the base_dn using SCOPE_SUBTREE to include the
        objects and all its descendants.

* get_all_persons(self) -> list:
    * Return all entries with the objectClass of 'person

* get_all_emails(self) -> dict:
    * Return a dictionary of all email (mail) addresses from entries with
        the objectClass of 'person.' The dictionary contains two keys. The
        first key is "emails," and its value is a list of emails. The second key is
        "errors" and its value is a list of returned entries that did not
        include email addresses. 

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [python3](https://docs.python.org/3.8/)
* [python-ldap](https://www.python-ldap.org/en/python-ldap-3.3.0/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
<!-- ## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps. -->

<!-- ### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ``` -->

<!-- ### Installation

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/github_username/repo_name.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```

<p align="right">(<a href="#top">back to top</a>)</p>
 -->


<!-- USAGE EXAMPLES -->
<!-- ## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#top">back to top</a>)</p>
 -->


<!-- ROADMAP -->
<!-- ## Roadmap

- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
    - [ ] Nested Feature

See the [open issues](https://github.com/github_username/repo_name/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>
 -->


<!-- CONTRIBUTING -->
<!-- ## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>
 -->


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Michael Delgado - [LinkedIn profile](https://www.linkedin.com/in/mike-del/) - devmikedel@gmail.com

Project Link: [https://github.com/dev-mike-del/ldap_operations](https://github.com/dev-mike-del/ldap_operations)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
<!-- ## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#top">back to top</a>)</p> -->



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/dev-mike-del/ldap_operations.svg?style=for-the-badge
[contributors-url]: https://github.com/dev-mike-del/ldap_operations/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/dev-mike-del/ldap_operations.svg?style=for-the-badge
[forks-url]: https://github.com/dev-mike-del/ldap_operations/network/members
[stars-shield]: https://img.shields.io/github/stars/dev-mike-del/ldap_operations.svg?style=for-the-badge
[stars-url]: https://github.com/dev-mike-del/ldap_operations/stargazers
[issues-shield]: https://img.shields.io/github/issues/dev-mike-del/ldap_operations.svg?style=for-the-badge
[issues-url]: https://github.com/dev-mike-del/ldap_operations/issues
[license-shield]: https://img.shields.io/github/license/dev-mike-del/ldap_operations.svg?style=for-the-badge
[license-url]: https://github.com/dev-mike-del/ldap_operations/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/mike-del
[forumSystems-screenshot]: screen_shots/forumSystems.png
[python_interpreter_example-screenshot]: screen_shots/python_interpreter_example.png
