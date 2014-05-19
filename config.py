config = {

    ##################
    # SQL Management #
    ##################

    "sql": {
        # SQL server's IP.
        # Is a string, not an integer.
        "host": 'localhost',

        # SQL username.
        "username": 'root',

        # SQL password.
        "password": 'password',

        # SQL database name.
        "database": 'database_name',
    },

    ####################
    # Website Management #
    ####################

    "website": {
        # Website's server IP.
        # Is a string, not an integer.
        "serverIP": '127.0.0.1',

        # URL to your website.
        # Does not end in '/'.
        "url": 'http://localhost',

        # Name of your website.
        "name": 'turtlebook',

        # Description of your website.
        "description": 'social network for turtle enthusiasts',

        # Email where people can send mail to you .
        "email": 'turtles.pl',

        # Is maintenance enabled?
        # Is a boolean, not a string.
        "maintenence": False,

        # Mainenance message.
        # Will only be shown if mainenance is enabled.
        "maint_message": 'turtlebook will be back soon!',

        # Template
        "template": 'template_name'
    },

    ###########################
    # Registration Management #
    ###########################

    "registration": {

        # Minimum and maximum character length for
        # usernames when registering.
        "maxmin_character_count": [3, 12]

    }
}
