@ stdcall RegConnectRegistryA(str long ptr) advapi32.RegConnectRegistryA
@ stdcall RegConnectRegistryW(wstr long ptr) advapi32.RegConnectRegistryW
@ stdcall RegCopyTreeA(long str long) kernelbase.RegCopyTreeA
@ stdcall RegCreateKeyA(long str ptr) advapi32.RegCreateKeyA
@ stdcall RegCreateKeyTransactedA(long str long ptr long long ptr ptr ptr long ptr) kernelbase.RegCreateKeyTransactedA
@ stdcall RegCreateKeyTransactedW(long wstr long ptr long long ptr ptr ptr long ptr) kernelbase.RegCreateKeyTransactedW
@ stdcall RegCreateKeyW(long wstr ptr) advapi32.RegCreateKeyW
@ stdcall RegDeleteKeyA(long str) advapi32.RegDeleteKeyA
@ stdcall RegDeleteKeyTransactedA(ptr str long long ptr ptr) kernelbase.RegDeleteKeyTransactedA
@ stdcall RegDeleteKeyTransactedW(ptr wstr long long ptr ptr) kernelbase.RegDeleteKeyTransactedW
@ stdcall RegDeleteKeyValueA(long str str) advapi32.RegDeleteKeyValueA
@ stdcall RegDeleteKeyValueW(long wstr wstr) advapi32.RegDeleteKeyValueW
@ stdcall RegDeleteKeyW(long wstr) advapi32.RegDeleteKeyW
@ stdcall RegDisablePredefinedCache() advapi32.RegDisablePredefinedCache
@ stdcall RegEnumKeyA(long long ptr long) advapi32.RegEnumKeyA
@ stdcall RegEnumKeyW(long long ptr long) advapi32.RegEnumKeyW
@ stdcall RegOpenKeyA(long str ptr) advapi32.RegOpenKeyA
@ stdcall RegOpenKeyTransactedA(ptr str long long ptr ptr ptr) kernelbase.RegOpenKeyTransactedA
@ stdcall RegOpenKeyTransactedW(ptr wstr long long ptr ptr ptr) kernelbase.RegOpenKeyTransactedW
@ stdcall RegOpenKeyW(long wstr ptr) advapi32.RegOpenKeyW
@ stdcall RegOverridePredefKey(long long) advapi32.RegOverridePredefKey
@ stdcall RegQueryMultipleValuesA(long ptr long ptr ptr) advapi32.RegQueryMultipleValuesA
@ stdcall RegQueryMultipleValuesW(long ptr long ptr ptr) advapi32.RegQueryMultipleValuesW
@ stdcall RegQueryValueA(long str ptr ptr) advapi32.RegQueryValueA
@ stdcall RegQueryValueW(long wstr ptr ptr) advapi32.RegQueryValueW
@ stdcall RegReplaceKeyA(long str str str) advapi32.RegReplaceKeyA
@ stdcall RegReplaceKeyW(long wstr wstr wstr) advapi32.RegReplaceKeyW
@ stdcall RegSaveKeyA(long ptr ptr) advapi32.RegSaveKeyA
@ stdcall RegSaveKeyW(long ptr ptr) advapi32.RegSaveKeyW
@ stdcall RegSetKeyValueA(long str str long ptr long) advapi32.RegSetKeyValueA
@ stdcall RegSetKeyValueW(long wstr wstr long ptr long) advapi32.RegSetKeyValueW
@ stdcall RegSetValueA(long str long ptr long) advapi32.RegSetValueA
@ stdcall RegSetValueW(long wstr long ptr long) advapi32.RegSetValueW
