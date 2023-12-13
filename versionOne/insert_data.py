from versionOne.models import Eventdetails

new_event = Eventdetails.objects.create( 
                            event='Year-end',
                            event_date = "1990-01-01",
                            location = "India",
                            description = "In the year 2023 end in India"
                        )
new_event.save()

from versionOne.models import Jobrequisition

new_event = Jobrequisition.objects.create( 
                            job_position='DS',
                            event_date = "1990-01-01",
                            location = "India",
                            description = "In the year 2023 end in India for DS position."
                        )
new_event.save()

from versionOne.models import Persona

new_event = Persona.objects.create( 
                    persona = "Test"
                    )

new_event.save()


from versionOne.models import Screeningmode

new_event = Screeningmode.objects.create( 
                    screening_mode = "Yes"
                    )

new_event.save()


from versionOne.models import Gender

new_event = Gender.objects.create( 
                    gender = "male"
                    )

new_event.save()


from versionOne.models import Maritalstatus

new_event = Maritalstatus.objects.create( 
                    marital_status = "single"
                    )

new_event.save()


from versionOne.models import Employeedirectory

new_event = Employeedirectory.objects.create( 
                    referred_by = "emp-1"
                    )

new_event.save()


from versionOne.models import Experiencelevel

new_event = Experiencelevel.objects.create( 
                    experience_level = "6 years"
                    )

new_event.save()


from versionOne.models import Educationlevel

new_event = Educationlevel.objects.create( 
                    education_level = "B.E"
                    )

new_event.save()


from versionOne.models import Reasonforchange

new_event = Reasonforchange.objects.create( 
                    reason_for_change = "Career_Growth"
                    )

new_event.save()


from versionOne.models import City

new_event = City.objects.create( 
                    city = "Chennai"
                    )

new_event.save()