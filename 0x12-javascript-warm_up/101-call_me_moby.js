#!/usr/bin/node
function executeFunctionXTimes (x, theFunction) {
  if (x > 0) {
    theFunction();
    executeFunctionXTimes(x - 1, theFunction);
  }
}
