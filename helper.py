# Helper functions

# Helper function for checking the equality of values in two tuples
# (this ignores the ordering of values in the tuples)
def tuple_val_eq(t1, t2):
	# Check if tuples are equals
	if t1 == t2: return True

	# Reverse the first tuple and check again
	(a, b) = t1
	return (b, a) == t2
