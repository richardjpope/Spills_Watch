import django
from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
import spill_watch.management.scraperwiki as scraperwiki
from spill_watch import models

# this command looks like a botch.  why isn't this data updated when it's run

class Command(BaseCommand):
    help = 'Update various meta data for a scraper or all scrapers.'

    def handle(self, **options):
        scraperwiki_api_short_name = 'us-national-response-center-incidents'

        data = scraperwiki.getData(scraperwiki_api_short_name)
        for item in data:

            #get company for this item
            test = models.Company.objects.filter(name = item['RESPONSIBLE_COMPANY'])
            item_company = None
            if len(test) == 1:
                item_company = test[0]
            else:
                #add new company?
                if item['RESPONSIBLE_COMPANY'] != '':
                    print "saving new company: " + item['RESPONSIBLE_COMPANY']
                    item_company = models.Company(name=item['RESPONSIBLE_COMPANY'])
                    item_company.save()


            #work out title
            if len(item['DESCRIPTION_OF_INCIDENT'])	<= 100:
                title = item['DESCRIPTION_OF_INCIDENT']
            else:
                title = item['DESCRIPTION_OF_INCIDENT'][:99]
                            
            #work out description
            description = item['DESCRIPTION_OF_INCIDENT'] + '\n + ' + item['ADDITIONAL_INFO']

            #add incident
            incident = models.Incident(title=title, description=description, company=item_company, incident_date=item['INCIDENT_DATE_TIME'], reported_date=item['DATE_TIME_RECEIVED'], action_taken = item['DESC_REMEDIAL_ACTION'])
            incident.save()
            

