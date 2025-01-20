| User action         | name | ingredient | complexity | location        | opening times | system action         |
| :------------------ | :--: | :--------- | :--------- | :-------------- | :------------ | :-------------------- |
| greet               |  -   | ?          | ?          | ?               | ?             | ask for name          |
| greet               |  x   | ?          | ?          | ?               | ?             | greet                 |
| declareName         |  x   | ?          | ?          | ?               | ?             | request task          |
| requestRecipe       |  ?   | -          | ?          | ?               | ?             | askforingredient      |
| requestRecipe       |  ?   | ?          | -          | ?               | ?             | ask for complexity    |
| requestRecipe       |  ?   | x          | x          | ?               | ?             | declareRecipe         |
| requestMarket       |  ?   | ?          | ?          | -               | ?             | ask for location      |
| requestmarket       |  ?   | ?          | ?          | = "the nearest" | ?             | ask is this city      |
| requestMarket       |  ?   | ?          | ?          | x               | ?             | declareMarket         |
| requestOpeningTimes |  ?   | ?          | ?          | -               | ?             | ask for location      |
| requestOpeningTimes |  ?   | ?          | ?          | x               | ?             | declare opening times |
