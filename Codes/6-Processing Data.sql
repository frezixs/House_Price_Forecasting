/* Deleting Columns */
ALTER TABLE deal_beijing 
DROP COLUMN index;

ALTER TABLE deal_shanghai
DROP COLUMN index;

ALTER TABLE selling_beijing
DROP COLUMN index;

ALTER TABLE selling_guangzhou 
DROP COLUMN index;

ALTER TABLE selling_shanghai
DROP COLUMN index;

/* Merge Selling */
Select * into Selling from selling_beijing 
union all
Select * from selling_shanghai
union all
Select * from selling_guangzhou	

/* Merge Deals */
Select * into Deal from deal_beijing 
union all
Select * from deal_shanghai


