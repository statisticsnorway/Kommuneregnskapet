CharacterReCode = function(x,oldLevels, newLevels){
  x = as.factor(x)
  le = levels(x)
  ma = match(le,oldLevels)
  isMatch = !is.na(ma)
  le[isMatch] = newLevels[ma[isMatch]]
  levels(x) = le
  as.character(x)
}

NaToZero <- function(x,warn=NULL){
  if(!anyNA(x)) return(x)
  if(!is.null(warn)) warning(warn)
  x[is.na(x)] <- 0
  x
}