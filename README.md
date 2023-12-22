Due to <https://github.com/pypa/pipx/discussions/1162>, this doesn't work in its intended form yet:

```
$ ./scripts.py format
All done! ✨ 🍰 ✨
4 files left unchanged.
```

For now, you have to:

```
$ poetry run python scripts.py format
All done! ✨ 🍰 ✨
4 files left unchanged.
```
