guest_list = ['bob', 'jeff', 'joe', 'jack']

#Invite people over
for guest in guest_list:
    print(f'\nHi {guest.title()}\nWould you like to come over\nThanks')

#State who can not make it 
print(f"\n{guest_list[1].title()} can't make it")

#Change the guest list
guest_list[1] = 'lewis'

#Send out new invites
for guest in guest_list:
    print(f'\nHi {guest.title()}\nWould you like to come over\nThanks')

#Add more to the guest list
guest_list.insert(0, 'Will')
guest_list.insert(2, 'Tom')
guest_list.insert(4, 'Phil')

#Send out new invites
for guest in guest_list:
    print(f'\n\nHi {guest.title()}\nWould you like to come over\nThanks')

#Amount of people coming
print(f'\nThere are {len(guest_list)} people coming tonight')

#Uninvite people 
for uninvited_people in range(5):
    uninvited_people = guest_list.pop()
    print(f'\n{uninvited_people.title()}, sorry you are no longer able to come')

#Let the last people know they are still coming
for guest in guest_list:
    print(f'\n\nHi {guest.title()}\nYou can still come over\nThanks')

#Emtpy the list
guest_list.clear()

#Show the list empty
print(guest_list)