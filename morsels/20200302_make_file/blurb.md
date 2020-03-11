First I tried to use `tempfile.TemporaryFile`, but it didn't let me handle closing manually as nicely as `tempfile.mkstemp`

From there, everything is a pretty easy passthrogh to `mkstemp` and `open`.
