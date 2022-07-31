# potionbartergame
The game is centred around the titular Potions, and contains 3 groups of people: 

● Vendors working for the company PotionCorp

● Adventurers, looking to buy Potions 

● You, the player, attempting to be the man-in-the-middle of this transaction.


The aim of this game is to buy potions from the vendors, and sell these to the adventurers for big profits. 
On any given day, our aim is to find discrepancies between the adventurers buying price, and the vendors selling price. 
For example, we might buy 5 Litres of a Potion of Instant Health from the vendors for $25, and sell this to the adventurers for $125, for a profit of $100.
A few things are assumed about these groups: 

● The adventurers have access to infinite amounts of money- They will always buy a potion if we offer it to them, at the rate they specify. 

● The vendors have a shared inventory of Potions, supplied to them by PotionCorp.

A vendor can only sell a single potion at a time, but may choose any potion from the inventory that no other vendor is selling.
Each potion has the following attributes:

● A category - The type of potion sold (Healing, Damage, Buff, etc) 

● A name- Specifying the exact effects (“Potion of Minor Regeneration”, “Deadly Poison”, “Potion of Undying Strength”, etc) 

● A price per litre- The amount paid per litre, to purchase this potion from a vendor ($10/L, $23.5/L, etc). Note that one can buy fractional quantities of each potion (I can buy 250ml of the first potion for $2.5)

The selling price to adventurers changes day by day, and so will be covered later on. 
A potion is uniquely identified by its name. All buy prices of potions are unique.
The vendors, however, do not offer all items at all times. 
Each day, each vendor will only offer 1 item from this inventory.

The game is played over multiple days, and each day progresses as follows: 
1. Certain potions/quantities are added to the inventory of the vendors by PotionCorp. 
2. Each vendor picks a single potion from the inventory to offer (Which is different from that of every other vendor) 
3. The player can purchase potions from the vendors
4. The player can sell potions to the adventurers for profits
