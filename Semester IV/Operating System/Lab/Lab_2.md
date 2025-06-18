# 🐧 Linux File Permissions & File Operations

## 🔐 Types of Permissions and Modes

Linux files/directories have 3 types of permissions:

| Symbol | Meaning |
|--------|---------|
| r      | Read    |
| w      | Write   |
| x      | Execute |

For 3 categories:

| Category | Who |
|----------|-----|
| User     | u   |
| Group    | g   |
| Others   | o   |

### Numeric Mode Representation:

| Permission | Binary | Value |
|------------|--------|-------|
| ---        | 000    | 0     |
| --x        | 001    | 1     |
| -w-        | 010    | 2     |
| -wx        | 011    | 3     |
| r--        | 100    | 4     |
| r-x        | 101    | 5     |
| rw-        | 110    | 6     |
| rwx        | 111    | 7     |

Example: `chmod 755 file` = rwx (7) for user, r-x (5) for group, r-x (5) for others.

---

## 📁 1. Create 4 Directories, Each with 4 Text Files

```bash
mkdir dir1 dir2 dir3 dir4
touch dir1/text1.txt dir1/text2.txt dir1/text3.txt dir1/text4.txt
touch dir2/text1.txt dir2/text2.txt dir2/text3.txt dir2/text4.txt
touch dir3/text1.txt dir3/text2.txt dir3/text3.txt dir3/text4.txt
touch dir4/text1.txt dir4/text2.txt dir4/text3.txt dir4/text4.txt
```

✅ **Result:** 4 folders with 4 text files in each.

---

## ✏️ 2. Rename `text1.txt` in dir1 to `text11.txt`

```bash
mv dir1/text1.txt dir1/text11.txt
```

✅ **Result:** `text1.txt` becomes `text11.txt` in `dir1`.

---

## ✏️ 3. Rename `dir1` to `dir_one`

```bash
mv dir1 dir_one
```

✅ **Result:** `dir1` is now renamed to `dir_one`.

---

## 📦 4. Move second file of dir3 to dir2

```bash
mv dir3/text2.txt dir2/
```

✅ **Result:** `text2.txt` from `dir3` moved to `dir2`.

---

## 📄 5. Copy all 4 files of dir_one to dir2

```bash
cp dir_one/*.txt dir2/
```

✅ **Result:** All `.txt` files from `dir_one` copied to `dir2`.

---

## 📁 6. Copy whole `dir3` to `dir2`

```bash
cp -r dir3 dir2/
```

✅ **Result:** `dir3` (with its contents) is copied into `dir2`.

---

## 🔄 7. Changing Modes and Permissions Examples

### Change permission to read-only for everyone:

```bash
chmod 444 dir2/text1.txt
```

✅ **Result:** Only read permission for all (r--r--r--).

---

### Give execute permission to user:

```bash
chmod u+x dir2/text1.txt
```

✅ **Result:** User can now execute it (r-xr--r--).

---

### Remove write permission from group:

```bash
chmod g-w dir2/text2.txt
```

✅ **Result:** Group cannot write anymore.

---

### Make file accessible to everyone:

```bash
chmod 777 dir2/text3.txt
```

✅ **Result:** Full access for user, group, and others.

---

## 🧹 Extra: Removing Files and Directories

### Remove a file:

```bash
rm dir2/text4.txt
```

### Remove an empty directory:

```bash
rmdir dir4
```

### Remove a directory with contents:

```bash
rm -r dir4
```

---

> 💡 Tip: Always be cautious when using `rm -r`, especially with `sudo`, to avoid deleting critical files.

---

✅ **Done!** You now know how to manage files, directories, and permissions in Linux! 🎉
