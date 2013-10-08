# gnome-shell-google-calendar

Google Calendar Daemon for GNOME Shell


## What is it?

A D-Bus service that fetches events from Google Calendar and makes them
available for GNOME Shell to display.

## What do I need?

Python 2.6+ with the following modules:
    gtk
    dbus
    gdata
    iso8601

Packages:
    gtk-engines
    gtk-engine-murrine
    gtk-engine-equinox


## Usage

Run the daemon like so:

    ./gnome-shell-google-calendar.py

You will be prompted for your Google Calendar email the
first time. A password is not neccesary, as gnome-online-accounts is used.

Once logged in, events from all your calendars should appear in
GNOME Shell's calendar.

To exclude calendars, create a file named "excludes" in the directory
you run "gnome-shell-google-calendar" from, or a file named
".gnome-shell-google-calendar-excludes" in your home directory.
List the title of each calendar you want to exclude on a separate
line.


## Excluding Calendars

On first run, the daemon will create the following file for you, it will be blank.

`~/.config/gnome-shell-calendar/config.yaml`

When you want to exclude certain calendars, simply :

1. open it up in your favourite text editor
2. find the 'exclusions' key
3. add the calendar names which you want to exclude as list items


for example:

```
- exclusions:
  - Birthdays
  - "The house that john built"
  - "Loan repayments"
```

