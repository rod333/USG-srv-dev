'''
Allows us to integrate with cal.models.Event

Should be a Manager, but we really, really don't care since we want to put
this in pom/ and not cal/.
'''
from cal.models import Event
from pom.bldg_info import *
import datetime, time
from django.db.models import Q
from utils.scrape import log

    
def all():
    '''
    Get all events
    '''
    return Event.objects.all().order_by('event_date_time_start','event_date_time_end')


def filter_by_bldg(qset, bldg_code):
    '''
    Get all events for `bldg_code`
    '''
    if qset:
        return qset.filter(event_location=bldg_code).order_by('event_date_time_start','event_date_time_end')
    else:
        return Event.objects.filter(event_location=bldg_code).order_by('event_date_time_start','event_date_time_end')


def filter_by_date(qset, leftMonth, leftDay, leftYear, leftHour, rightMonth, rightDay, rightYear, rightHour):
    '''
    OLD: Get all events between a range of dates
    '''
    left = datetime.datetime(year = int(leftYear), month = int(leftMonth), day = int(leftDay), hour = int(leftHour))
    right = datetime.datetime(year = int(rightYear), month = int(rightMonth), day = int(rightDay), hour = int(rightHour))
    if qset:
        return qset.filter(event_date_time_start__gte=left, event_date_time_end__lte=right).order_by('event_date_time_start','event_date_time_end')
    else:
        return Event.objects.filter(event_date_time_start__gte=left, event_date_time_end__lte=right).order_by('event_date_time_start','event_date_time_end')


def filter_by_day_hour(qset, leftDate, rightDate, leftHour, leftMinutes, rightHour, rightMinutes):
    '''
    Get all events between a range of dates and hours within those dates
    See the timeline to visualize what this means.
    Special case: If end time is 12:00 AM, then assume it means the 12:00 AM of the day after the end day
    '''
    
    left = leftDate.replace(hour=int(leftHour), minute=int(leftMinutes))
    right = rightDate.replace(hour=int(rightHour), minute=int(rightMinutes))
    if rightHour == 0 and rightMinutes == 0:
        right += datetime.timedelta(days = 1)

    if qset:
        temp = qset.filter(event_date_time_start__gte=left, event_date_time_end__lte=right).order_by('event_date_time_start','event_date_time_end')
    else:
        temp = Event.objects.filter(event_date_time_start__gte=left, event_date_time_end__lte=right).order_by('event_date_time_start','event_date_time_end')
    
    retlist = []
    for x in temp:
        if (int(rightHour) > int(leftHour)):
            if x.event_date_time_start.hour >= int(leftHour) and x.event_date_time_start.hour <= int(rightHour):
                if (x.event_date_time_start.hour == int(rightHour)):
                    if (x.event_date_time_start.minute <= int(rightMinutes)):
                        retlist.append(x)
                elif x.event_date_time_start.hour == int(leftHour):
                    if (x.event_date_time_start.minute >= int(leftMinutes)):
                        retlist.append(x)
                else:
                        retlist.append(x)
        else:
            if (x.event_date_time_start.hour >= int(leftHour) or x.event_date_time_start.hour <= (int(rightHour)%24)):
                if (x.event_date_time_start.hour == int(rightHour)):
                    if (x.event_date_time_start.minute <= int(rightMinutes)):
                        retlist.append(x)
                elif x.event_date_time_start.hour == int(leftHour):
                    if (x.event_date_time_start.minute >= int(leftMinutes)):
                        retlist.append(x)
                else:
                        retlist.append(x)
    return retlist


def filter_by_search(qset, query):
    '''
    Get all events with `query` in their title or description
    '''
    if not query: return qset
    if qset:
        return qset.filter(Q(event_cluster__cluster_title__icontains=query) |
                           Q(event_clusert__cluster_description__icontains=query))
    else:
        return Event.objects.filter(Q(event_cluster__cluster_title__icontains=query) |
                                    Q(event_cluster__cluster_description__icontains=query))
        
        
