---
icon: material/cart
---
<!-- quelle: de/handel.md · stand: c6fa2c77c86e · fassung: maschinell -->

# Trade

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../bilder/kopf/handel.png">
  <img src="../bilder/kopf/handel_hell.png" alt="Bannerbild: die Überschrift „Handel“ neben einer gebauten Warenkorb-Übersicht mit Positionen und Endsumme.">
</picture>

!!! info "Machine translation"

    This page was translated automatically from the German original. Wording may be imprecise; the German version is authoritative.

**Six building blocks** for trade information: price, product, shopping cart, voucher, rating,
Wishlist.

This allows product overviews, shopping cart views and rating displays
as part of a larger area or on its own.

## What's there

| Module | Shows |
| --- | --- |
| Product card | a product with image, description and price |
| Price indication | a price, possibly with a strike price |
| Cart | Items, Tax, Shipping and Total |
| Review overview | Average and distribution of reviews |
| Coupon field | a coupon code |
| Wishlist | flagged products |

## What these building blocks are — and what they are not

**They represent.** They do not settle an order, they do not talk to any payment service,
and they don't run a merchandise management system. A shopping cart shows a sum; it collects it
not.

This is not a limitation that could be fixed casually — payment processing is a
own field with own obligations. If you need something like that, you need a connection to
a system that can.

**What they are good for:** an overview of your own products, a comparison of offers, a
Representation of data that comes from elsewhere — wherever there is something to do with prices,
but nothing is sold.

## What is honestly open here

- Voucher field and watch list are still scaffolding: they display, but do not yet bring
operation. They are marked as such in the directory.
- There is no currency conversion and no tax logic. What is stored is displayed.
- There is no connection to sales platforms or merchandise management.

---

All six modules are in the [module directory](../de/typen/commerce.md).