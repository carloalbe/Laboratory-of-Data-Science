# Part 3
``` .mdx
--Show the percentage increase in total sales with respect to the previous month for
--each ram brand and each country.
with 
  member previous as 
    ([Time].[DayMonthQuarterYear].currentMember.lag(1), [Measures].[Sales Usd])
  member perc as 
    ([Measures].[Sales Usd] - previous)/ previous , 
    format_string="percent" 
 select {[Measures].[Sales Usd],previous,perc} on axis(0),
 NonEmptyCrossJoin([Ram Product].[NameBrand].[Brand],[Geography].[Country].[Country],[Time].[DayMonthQuarterYear].[Month Quarter Year])on axis(1) from [Group17HW Mart];
 ```
