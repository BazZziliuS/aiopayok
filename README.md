[![GitHub issues](https://img.shields.io/github/issues/bazzzilius/aiopayok?style=for-the-badge)](https://github.com/bazzzilius/aiopayok/issues)
[![GitHub license](https://img.shields.io/github/license/bazzzilius/aiopayok?style=for-the-badge)](https://github.com/bazzzilius/aiopayok/blob/main/LICENSE)
[![PyPI old](https://img.shields.io/pypi/v/aiopayok?style=for-the-badge)](https://pypi.org/project/aiopayok/)
## AIOPayok

>payok.io asynchronous python wrapper <br>
>The original project was abandoned, which is why I hope you will support a copy of it.
``` python
import asyncio

from aiopayok import Payok


payok = Payok("API_ID", "API_KEY")


async def main() -> None:
    print(await payok.get_balance())

asyncio.run(main())

```

### Installing

``` bash
pip install aiopayok
```

### Resources

- Check out the docs at https://payok.io/cabinet/documentation/doc_main.php to learn more about PayOk,
