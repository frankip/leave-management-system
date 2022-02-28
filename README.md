# leave-management-system
A simple leave management system that allows user to list, submit, and edit leave request

<!-- GETTING STARTED -->
## Getting Started

You will need a few prerequisite to run the project locally

### Prerequisites

* python 
  ```sh
  - python 3 
  - pip
  ```

### Installation


1. Clone the repo
   ```sh
   git clone https://github.com/frankip/leave-management-system.git
   ```
2. create a virtual environment and activate it
   ```sh
   python3 -m venv venv

   and activate

   source venv/bin/activate
   ```
3. install project dependencies
   ```py
   pip install -r requirements.txt
   ```
4. run migrations
   ```py
   python manage.py migrate
   ```

5. create a super user and put your password
   ```py
   python manage.py createsuperuser --username=admin
   ```
6. start the project
   ```py
   python manage.py runserver
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage


|  paths 	            |   views	                    |
|-----------------------|-------------------------------|
|   `leave/` 	         | view all leave request   	  |
|   `leave/id/`         | view single leave request     |
|   `leave/add/`	      | request a new leave  	        |
|   `leave/id/edit/`    | edit a single leave request   | 
|   `leave/id/delete/`  | delete a single leave request |

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [Francis Kipchumba](https://github.com/frankip) 

Project Link: [https://github.com/frankip/leave-management-system](https://github.com/frankip/leave-management-system)

<p align="right">(<a href="#top">back to top</a>)</p>


