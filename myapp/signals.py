from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init, post_init, pre_save, post_save, pre_delete, post_delete, pre_migrate, post_migrate
from django.core.signals import request_started, request_finished, got_request_exception
from django.db.backends.signals import connection_created


@receiver(user_logged_in, sender=User) #we don't have to use connector when we use recevier decorator
def login(sender, request, user, **kwargs): #this is a receiver function
    print("_________________________-------___________")
    print("logged in signal")
    print(f"sender: {sender}")
    print(f"request: {request}")
    print(f"user: {user}")
    print(f"user_username: {user.username}")
    print(f"user_email: {user.email}")
    print(f"user_password: {user.password}")
    print(f"kwargs: {kwargs}")

# user_logged_in.connect(login, sender=User)

@receiver(user_logged_out, sender=User)
def logout(sender, request, user, **kwargs): #this is a receiver function
    print("_________________________-------___________")
    print("logged out signal")
    print(f"sender: {sender}")
    print(f"request: {request}")
    print(f"user: {user}")
    print(f"user_username: {user.username}")
    print(f"user_email: {user.email}")
    print(f"user_password: {user.password}")
    print(f"kwargs: {kwargs}")

@receiver(user_login_failed)
def login_failed(sender, credentials, request, **kwargs): #this is a receiver function
    print("_________________________-------___________")
    print("login failed signal")
    print(f"sender: {sender}")
    print(f"credentials: {credentials}")
    print(f"request: {request}")
    print(f"kwargs: {kwargs}")

# *****************************pre_save and post_save signals*******************************

# @receiver(pre_save, sender=User)
def first_save(sender, instance, **kwargs):    
    print("******************")
    print("inside pre_save signal")
    print(f"sender: {sender}")
    print(f"instance: {instance}")
    print(f"kwargs: {kwargs}")

pre_save.connect(first_save, sender=User)    

@receiver(post_save, sender=User)
def post_save(sender, instance, created, **kwargs):    
    print("******************")
    if created:
        print("inside post_save signal")
        print("created_new record")
        print(f"sender: {sender}")
        print(f"instance: {instance}")
        print(f"created: {created}")
        print(f"kwargs: {kwargs}")
    else:
        print("post_save signal")
        print("update")
        print(f"sender: {sender}")
        print(f"instance: {instance}")
        print(f"created: {created}")
        print(f"kwargs: {kwargs}")
# post_save.connect(first_save, sender=User)    


# *********************************pre_delete and post_delete signals *************************


@receiver(pre_delete, sender=User)
def before_delete(sender, instance, **kwargs):    
    print("******************")
    print("inside pre_delete signal")
    print(f"sender: {sender}")
    print(f"instance: {instance}")
    print(f"kwargs: {kwargs}")



@receiver(post_delete, sender=User)
def after_delete(sender, instance, **kwargs):    
    print("******************")
    print("post_delete signal")
    print(f"sender: {sender}")
    print(f"instance: {instance}")
    print(f"kwargs: {kwargs}")

# **********************pre_init and post_init signals *******************************
# this signals gets activated whenever any models get intantiate

@receiver(pre_init, sender=User)
def before_init(sender, *args, **kwargs):    
    print("******************")
    print("inside pre_init signal")
    print(f"sender: {sender}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")



@receiver(post_init, sender=User)
def after_init(sender, *args, **kwargs):    
    print("******************")
    print("inside post_init signal")
    print(f"sender: {sender}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")


# *************************request_started, request_finished and got_request_exception************

@receiver(request_started)
def at_request_start(sender, environ, **kwargs):
    print("**************************")
    print("inside request_started")
    print(f"sender : {sender}")
    print(f"environ : {environ}")
    print(f"kwargs : {kwargs}")

@receiver(request_finished)
def at_request_finished(sender, **kwargs):
    print("**************************")
    print("inside request_finished")
    print(f"sender : {sender}")
    print(f"kwargs : {kwargs}")

@receiver(got_request_exception)
def at_request_exception(sender, request, **kwargs):
    print("**************************")
    print("inside got_request_exception")
    print(f"sender : {sender}")
    print(f"request : {request}")
    print(f"kwargs : {kwargs}")



# *********************************pre_migrate and post_migrate signals *************************




@receiver(pre_migrate)
def before_migrate(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):    
    print("******************")
    print("inside pre_migrate signal")
    print(f"sender: {sender}")
    print(f"app_config: {app_config}")
    print(f"verbosity: {verbosity}")
    print(f"interactive: {interactive}")
    print(f"using: {using}")
    print(f"plan: {plan}")
    print(f"apps: {apps}")
    print(f"kwargs: {kwargs}")



@receiver(post_migrate)
def after_init(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):    
    print("******************")
    print("inside post_migrate signal")
    print(f"sender: {sender}")
    print(f"app_config: {app_config}")
    print(f"verbosity: {verbosity}")
    print(f"interactive: {interactive}")
    print(f"using: {using}")
    print(f"plan: {plan}")
    print(f"apps: {apps}")
    print(f"kwargs: {kwargs}")

# ********************************************connection_created signal ********************    
# Database wrapper: signals sent by databse wrapper when a db connection is initiated

@receiver(connection_created)
def before_init(sender, connection, **kwargs):    
    print("******************")
    print("inside pre_init signal")
    print(f"sender: {sender}")
    print(f"connection: {connection}")
    print(f"kwargs: {kwargs}")

