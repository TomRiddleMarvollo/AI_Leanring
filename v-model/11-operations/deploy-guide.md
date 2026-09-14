# Deployment Guide — Hướng dẫn triển khai

> Cho **người vận hành**: đưa phần mềm lên môi trường & cấu hình. _For operators: how to deploy & configure._
> "Chạy được trên máy tôi" ≠ giao được — mục này buộc nghĩ tới môi trường thật.

## Môi trường — Environments
| Môi trường | URL / Host | Ghi chú |
|-----------|------------|---------|
| staging | _..._ | dữ liệu test |
| production | _..._ | dữ liệu thật |

## Yêu cầu hệ thống — Prerequisites
_(runtime/phiên bản, DB, biến môi trường bắt buộc — đối chiếu `.env.example`, KHÔNG commit secret.)_

## Các bước triển khai — Steps
1. _(build / migrate DB / deploy / health-check)_
2. _(...)_

## Cấu hình — Configuration
_(Biến môi trường, feature flag, secret lấy từ đâu — vault/CI, không hardcode.)_

## Rollback
_(Cách quay lui phiên bản trước + hoàn tác migration nếu cần.)_

## Checklist review chất lượng — Quality review
- [ ] Người mới theo được **không cần hỏi**; các bước lặp lại được.
- [ ] Nêu **biến môi trường & secret** (nguồn lấy), không lộ secret.
- [ ] Có **health-check sau deploy** và **cách rollback**.
