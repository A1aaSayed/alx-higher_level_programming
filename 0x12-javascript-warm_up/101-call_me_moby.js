#!/usr/bin/node
exports.callMeMoby = function callMeMoby (x, theFunction) {
    if (x > 0) {
      theFunction();
      callMeMoby (x - 1, theFunction);
    }
};
